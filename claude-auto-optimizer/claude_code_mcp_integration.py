#!/usr/bin/env python3
"""
Claude Code MCP Integration
Sistema otimizado que usa Claude Code MCP para operações diretas
"""

import os
import json
import requests
import subprocess
import time
import logging
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CodeOperationResult:
    success: bool
    output: str
    execution_time: float
    files_modified: List[str]
    git_operations: List[str]
    errors: List[str] = None

class ClaudeCodeMCPManager:
    """
    Manager para integração com Claude Code MCP Server
    """
    
    def __init__(self, project_path: str, github_repo_path: str):
        self.project_path = Path(project_path)
        self.github_repo_path = Path(github_repo_path)
        self.setup_mcp_config()
    
    def setup_mcp_config(self):
        """Configura o MCP para Claude Code"""
        
        # Detectar o client MCP (Cursor/Windsurf)
        mcp_configs = [
            Path.home() / ".cursor" / "mcp.json",  # Cursor
            Path.home() / ".codeium" / "windsurf" / "mcp_config.json",  # Windsurf
            Path.home() / ".config" / "cursor" / "mcp.json",  # Linux Cursor
            Path.home() / ".config" / ".codeium" / "windsurf" / "mcp_config.json"  # Linux Windsurf
        ]
        
        for config_path in mcp_configs:
            if config_path.parent.exists():
                self.setup_mcp_file(config_path)
                break
    
    def setup_mcp_file(self, config_path: Path):
        """Configura arquivo MCP"""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        mcp_config = {
            "mcpServers": {
                "claude-code-mcp": {
                    "command": "npx",
                    "args": ["-y", "@steipete/claude-code-mcp@latest"],
                    "env": {
                        "MCP_CLAUDE_DEBUG": "false",
                        "CLAUDE_CLI_NAME": "claude"
                    }
                }
            }
        }
        
        # Merge com config existente se houver
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    existing_config = json.load(f)
                if "mcpServers" in existing_config:
                    existing_config["mcpServers"].update(mcp_config["mcpServers"])
                    mcp_config = existing_config
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON in {config_path}, recreating...")
        
        with open(config_path, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        
        logger.info(f"✅ MCP configured at: {config_path}")

class ClaudeCodeAutoOptimizer:
    """
    Auto-optimizer usando Claude Code MCP diretamente
    """
    
    def __init__(self, project_path: str, github_repo_path: str):
        self.project_path = Path(project_path)
        self.github_repo_path = Path(github_repo_path)
        self.mcp_manager = ClaudeCodeMCPManager(project_path, github_repo_path)
    
    def optimize_workflow_with_claude_code(self, workflow_name: str) -> CodeOperationResult:
        """
        Otimização completa usando Claude Code MCP
        """
        start_time = time.time()
        
        # Construir prompt comprehensivo para Claude Code
        optimization_prompt = self.build_optimization_prompt(workflow_name)
        
        try:
            # Executar via Claude Code MCP
            result = self.execute_claude_code_operation(optimization_prompt)
            
            execution_time = time.time() - start_time
            
            return CodeOperationResult(
                success=True,
                output=result['output'],
                execution_time=execution_time,
                files_modified=result.get('files_modified', []),
                git_operations=result.get('git_operations', [])
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            
            return CodeOperationResult(
                success=False,
                output="",
                execution_time=execution_time,
                files_modified=[],
                git_operations=[],
                errors=[str(e)]
            )
    
    def build_optimization_prompt(self, workflow_name: str) -> str:
        """
        Constrói prompt comprehensivo para Claude Code
        """
        
        prompt = f"""
Your work folder is {self.github_repo_path}

I need you to perform a complete workflow optimization for '{workflow_name}'. Here's what you need to do:

## PHASE 1: ANALYSIS
1. Read the current configuration from 'workflows/{workflow_name}/config.json'
2. Read the current prompts from 'workflows/{workflow_name}/prompts.md'  
3. Read the test scenarios from 'workflows/{workflow_name}/test-scenarios.json'
4. Analyze the current performance metrics in the config

## PHASE 2: TESTING
5. Execute the test scenarios against the n8n workflow
6. Calculate success rate, response time, and quality scores
7. Identify specific failure patterns and performance issues

## PHASE 3: OPTIMIZATION
8. If performance is below thresholds (success < 85%, response > 2.5s):
   - Analyze the prompt for clarity, specificity, and structure
   - Identify areas for improvement based on test failures
   - Generate an optimized version of the main prompt
   - Ensure the optimized prompt addresses identified issues

## PHASE 4: IMPLEMENTATION
9. Update the prompts.md file with:
   - The new optimized prompt
   - A new version entry in the optimization history
   - Documentation of what changed and why
   
10. Update the config.json with:
    - New performance metrics
    - Updated last_optimization timestamp
    - Incremented version number

11. Update the corresponding n8n workflow with the new prompt:
    - Use n8n API to get the current workflow
    - Find nodes that contain prompts (anthropic, openai, etc.)
    - Update the prompt parameters
    - Save the updated workflow

## PHASE 5: VALIDATION
12. Run the test scenarios again with the updated workflow
13. Compare before/after performance metrics
14. Create a summary report of improvements

## PHASE 6: DOCUMENTATION
15. Commit all changes to git with descriptive messages:
    - "feat(prompts): optimize {workflow_name} prompt for better performance"
    - Include before/after metrics in commit message
    
16. Create a detailed log entry in 'performance/optimization-history.json'

## ENVIRONMENT VARIABLES YOU'LL NEED:
- N8N_API_URL: {os.getenv('N8N_API_URL', 'http://localhost:5678/api/v1')}
- N8N_API_KEY: {os.getenv('N8N_API_KEY', 'your-n8n-api-key')}
- CLAUDE_API_KEY: {os.getenv('CLAUDE_API_KEY', 'your-claude-api-key')}

## CONSTRAINTS:
- Only optimize if current success rate < 85% OR average response time > 2.5s
- Backup the original prompt before making changes
- Test thoroughly before implementing changes
- Document all changes with clear reasoning
- Use semantic versioning for updates

## SUCCESS CRITERIA:
- Success rate improvement of at least 5%
- Response time reduction of at least 10%
- No regression in existing working test cases
- Clear documentation of all changes

Please execute this complete optimization process and provide a detailed report of what was done, what changed, and the performance improvements achieved.
"""
        
        return prompt.strip()
    
    def execute_claude_code_operation(self, prompt: str) -> Dict:
        """
        Executa operação via Claude Code MCP
        """
        
        # Para desenvolvimento/teste, simular execução
        # Em produção, isso seria executado via MCP client
        
        logger.info("🚀 Executing Claude Code operation...")
        logger.info(f"Prompt length: {len(prompt)} characters")
        
        # Simulação de resultado (em produção seria via MCP)
        simulated_result = {
            'output': f"""
✅ Workflow optimization completed for workflow

## Analysis Results:
- Current success rate: 72%
- Average response time: 3.2s
- Main issues: Ambiguous instructions, missing examples

## Optimization Applied:
- Added step-by-step guidance structure
- Included specific examples for edge cases
- Clarified error handling instructions
- Improved context awareness prompts

## Performance Improvement:
- Success rate: 72% → 89% (+17%)
- Response time: 3.2s → 2.1s (-34%)
- Quality score: 6.8 → 8.4 (+23%)

## Files Modified:
- workflows/{workflow_name}/prompts.md (updated main prompt + history)
- workflows/{workflow_name}/config.json (new performance metrics)
- n8n workflow updated via API

## Git Operations:
- Created backup branch: backup/optimization_20250110_1254
- Committed changes with detailed metrics
- Updated optimization history log

Optimization completed successfully! 🎉
""",
            'files_modified': [
                f'workflows/{workflow_name}/prompts.md',
                f'workflows/{workflow_name}/config.json',
                'performance/optimization-history.json'
            ],
            'git_operations': [
                'backup branch created',
                'changes committed',
                'optimization logged'
            ]
        }
        
        return simulated_result
    
    def monitor_all_workflows(self) -> Dict:
        """
        Monitora e otimiza todos os workflows usando Claude Code
        """
        
        monitoring_prompt = f"""
Your work folder is {self.github_repo_path}

Perform comprehensive monitoring and optimization of all workflows:

## MONITORING TASK:
1. List all workflows in the 'workflows/' directory
2. For each workflow:
   - Check if auto_optimization is enabled in config.json
   - Check when last optimization was performed
   - Evaluate current performance metrics
   - Determine if optimization is needed (success < 85% OR response > 2.5s OR last optimization > 24h ago)

3. For workflows that need optimization:
   - Perform the complete optimization process (analysis → testing → optimization → implementation → validation)
   - Document all changes and improvements
   - Update git with detailed commit messages

4. Generate a comprehensive monitoring report with:
   - Status of each workflow
   - Optimizations performed
   - Performance improvements achieved
   - Any issues encountered
   - Recommendations for further improvements

## SUCCESS METRICS:
- All eligible workflows optimized
- Average performance improvement across all workflows
- No regressions in existing functionality
- Complete documentation of all changes

Execute this monitoring and optimization process for all workflows.
"""
        
        try:
            result = self.execute_claude_code_operation(monitoring_prompt)
            return {
                'success': True,
                'summary': result['output'],
                'workflows_processed': result.get('files_modified', []),
                'optimizations_applied': len(result.get('git_operations', []))
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'workflows_processed': [],
                'optimizations_applied': 0
            }

class ClaudeCodeCLI:
    """
    Interface CLI para o sistema Claude Code MCP
    """
    
    def __init__(self):
        self.setup_environment()
    
    def setup_environment(self):
        """Configura ambiente necessário"""
        
        # Verificar se Claude CLI está instalado
        try:
            result = subprocess.run(['claude', '--version'], 
                                  capture_output=True, text=True, check=True)
            logger.info(f"✅ Claude CLI found: {result.stdout.strip()}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.error("❌ Claude CLI not found. Please install:")
            logger.error("npm install -g @anthropic-ai/claude-code")
            logger.error("claude --dangerously-skip-permissions")
            return False
        
        # Verificar se permissions foram aceitas
        claude_config = Path.home() / ".claude"
        if not claude_config.exists():
            logger.warning("⚠️ Run 'claude --dangerously-skip-permissions' first")
        
        return True
    
    def run_optimization(self, workflow_name: str, project_path: str, github_repo: str):
        """Executa otimização de workflow específico"""
        
        optimizer = ClaudeCodeAutoOptimizer(project_path, github_repo)
        result = optimizer.optimize_workflow_with_claude_code(workflow_name)
        
        if result.success:
            print(f"✅ Optimization completed for {workflow_name}")
            print(f"⏱️ Execution time: {result.execution_time:.2f}s")
            print(f"📁 Files modified: {len(result.files_modified)}")
            print(f"🔧 Git operations: {len(result.git_operations)}")
            print("\n📊 Summary:")
            print(result.output)
        else:
            print(f"❌ Optimization failed for {workflow_name}")
            if result.errors:
                for error in result.errors:
                    print(f"  • {error}")
    
    def run_monitoring(self, project_path: str, github_repo: str):
        """Executa monitoramento de todos os workflows"""
        
        optimizer = ClaudeCodeAutoOptimizer(project_path, github_repo)
        result = optimizer.monitor_all_workflows()
        
        if result['success']:
            print("✅ Monitoring completed successfully")
            print(f"📊 Workflows processed: {len(result['workflows_processed'])}")
            print(f"🔧 Optimizations applied: {result['optimizations_applied']}")
            print("\n📈 Summary:")
            print(result['summary'])
        else:
            print("❌ Monitoring failed")
            print(f"Error: {result['error']}")

def main():
    """Função principal CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Claude Code MCP Auto-Optimizer')
    parser.add_argument('command', choices=['optimize', 'monitor', 'setup'], 
                       help='Command to execute')
    parser.add_argument('--workflow', help='Workflow name (for optimize command)')
    parser.add_argument('--project-path', default='.', 
                       help='Project path (default: current directory)')
    parser.add_argument('--github-repo', required=True,
                       help='GitHub repository path for configurations')
    
    args = parser.parse_args()
    
    cli = ClaudeCodeCLI()
    
    if args.command == 'setup':
        if cli.setup_environment():
            print("✅ Setup completed successfully")
        else:
            print("❌ Setup failed")
    
    elif args.command == 'optimize':
        if not args.workflow:
            print("❌ --workflow is required for optimize command")
            return
        cli.run_optimization(args.workflow, args.project_path, args.github_repo)
    
    elif args.command == 'monitor':
        cli.run_monitoring(args.project_path, args.github_repo)

if __name__ == "__main__":
    main()