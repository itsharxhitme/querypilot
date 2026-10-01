import subprocess
import sys
def test_valid_arguments():
    
    
    
    result = subprocess.run(
        [
            sys.executable,"-m","querypilot.cli","--question","this is a demo question",
            "--config","/config"
            
        ],
        capture_output=True,
        text= True
    )
    
    assert result.returncode == 0 
    assert "this is a demo question" in result.stdout