# Docker Dangling Image Cleaner

This tool removes unused and untagged Docker images to free up space.


1. Why this is useful
This script automates a common system maintenance task. The standard command-line equivalent is docker image prune. 
However, a Python script provides several advantages: 

Automation: It can be scheduled to run automatically, for example, as a cron job, without manual intervention.
Logging: The script provides clear output on what it is doing and how many images are being removed, which is useful for monitoring and auditing.
Customisation: The script can be easily modified for more complex cleanup logic, such as removing images older than a certain date or implementing different filtering criteria.


2. Features

Detects dangling Docker images
Deletes only unused ones
Logs all actions (optional)
Can run as a scheduled job


3. How to check dangling image
docker images -f "dangling=true"

REPOSITORY     TAG       IMAGE ID       CREATED        SIZE
<none>        <none>    071dd73121e8   3 months ago   1.09GB



🖥️ 4. Usage Examples
Run manually:

### Shell version
```bash
bash clean-dangling-images.sh

## Python version
pip install -r requirements.txt
python clean_dangling.py


As a cron job:
4 46 * * * /path/to/clean-dangling-images.sh >> /var/log/docker-cleanup.log 2>&1

4. .gitignore
.venv/
__pycache__/
logs/
*.log

.gitignore is a special file used by Git to tell it which files and folders to ignore — meaning they will not be tracked or committed to the Git repository.


Project Structure (Optional)

docker-dangling-cleaner/
├── clean-dangling-images.sh
├── clean_dangling.py
├── README.md
├── requirements.txt
└── logs/



50 4 20 9 *  /Users/tom/Desktop/Devops/Project/Docker Dangling Image/clean-dangling-images.sh >> /var/log/docker-cleanup.log 2>&1

In this common scenario, >/dev/null first redirects stdout to /dev/null (a special device that discards all data written to it). Then, 2>&1 redirects stderr to stdout, 
effectively silencing all output and errors from the command.




