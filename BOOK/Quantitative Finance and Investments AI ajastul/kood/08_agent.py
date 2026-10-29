"""Ava agentimooduli CLI; vaikimisi offline, --agent lubab päris LLM-i."""
import runpy
from pathlib import Path
if __name__=='__main__':runpy.run_path(str(Path(__file__).with_name('07_rag_agent.py')),run_name='__main__')
