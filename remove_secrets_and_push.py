#!/usr/bin/env python3
"""
Script para remover secrets dos arquivos e fazer push limpo
"""

import os
import re

def remove_tokens_from_file(filepath, replacement="[TOKEN_REMOVIDO]"):
    """Remove tokens de um arquivo específico"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Patterns para diferentes tipos de tokens
        patterns = [
            r'ghp_[a-zA-Z0-9]{36}',  # GitHub Personal Access Token
            r'eyJ[a-zA-Z0-9\._-]*',   # JWT tokens (N8N)
            r'sk-[a-zA-Z0-9-_]{48}'   # API keys
        ]
        
        modified = False
        for pattern in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Tokens removidos de: {filepath}")
            return True
        
    except Exception as e:
        print(f"❌ Erro ao processar {filepath}: {e}")
    
    return False

def main():
    print("🔧 Removendo tokens sensíveis dos arquivos...")
    
    files_to_clean = [
        'CONFIG_TESTES_N8N.md',
        'claude-auto-optimizer/.env', 
        'claude-auto-optimizer/github_structure_creator.py',
        'claude-auto-optimizer/setup_gabriel.py.sh'
    ]
    
    cleaned_files = []
    for file in files_to_clean:
        if remove_tokens_from_file(file):
            cleaned_files.append(file)
    
    if cleaned_files:
        print(f"\n📁 Arquivos limpos: {len(cleaned_files)}")
        print("🔄 Fazendo commit dos arquivos sem tokens...")
        
        os.system('git add .')
        os.system('git commit -m "Remove tokens sensíveis dos arquivos para permitir push\n\n🔒 Tokens substituídos por placeholders\n🤖 Generated with [Claude Code](https://claude.ai/code)\n\nCo-Authored-By: Claude <noreply@anthropic.com>"')
        
        print("🚀 Tentando push...")
        result = os.system('git push -u origin master')
        
        if result == 0:
            print("✅ Push realizado com sucesso!")
        else:
            print("❌ Push ainda bloqueado")
    else:
        print("ℹ️ Nenhum arquivo precisou ser limpo")

if __name__ == '__main__':
    main()