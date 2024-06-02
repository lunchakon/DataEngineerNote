Bash programming is a valuable skill for data engineers,allowing you to automate tasks, interact with Linux systems, and build data pipelines.

## Top Tips

## Data Cleaning with Awk:
### This script cleans a CSV file by removing leading/trailing spaces and converting all characters to lowercase.

#!/bin/bash

#!/bin/bash

        # Input and output filenames (modify as needed)
        input_file="dirty_data.csv"
        output_file="clean_data.csv"

        awk -v OFS=, '
        {
            for (i=1; i<=NF; ++i) {
            gsub(/^\s+|\s+$/, "", $i);
            $i = tolower($i);
            }
            print
        }
        ' "$input_file" > "$output_file"

        echo "Data cleaned and saved to: $output_file"

## File Validation with Grep and Test:
### This script checks if a file exists and contains a specific pattern.

        #!/bin/bash

        # File to check and pattern to search
        target_file="important_data.txt"
        pattern_to_find="error message"

        # Check if file exists
        if [ ! -f "$target_file" ]; then
        echo "Error: File '$target_file' not found!"
        exit 1
        fi

        # Check for pattern using grep
        if grep -q "$pattern_to_find" "$target_file"; then
        echo "Warning: Pattern '$pattern_to_find' found in '$target_file'"
        fi

        echo "File '$target_file' exists and seems okay (no '$pattern_to_find' found)."

## Data Transformation with Sed:
### This script replaces a specific value in a file with another value.      

        #!/bin/bash

        # File to modify, old value, and new value
        target_file="config.ini"
        old_value="value1"
        new_value="value2"

        # Use sed to replace occurrences
        sed -i "s/$old_value/$new_value/g" "$target_file"

        echo "Replaced '$old_value' with '$new_value' in '$target_file'"


## Archiving Logs with Tar and Gzip:
### This script creates a compressed archive of log files older than a specified number of days.
        #!/bin/bash

        # Directory containing logs, number of days to keep, and archive name
        log_dir="/var/log"
        days_to_keep=7
        archive_name="logs_$(date +%Y-%m-%d).tar.gz"

        # Find logs older than specified days
        find "$log_dir" -type f -mtime +$days_to_keep -print | tar -czf "$archive_name" -

        echo "Logs older than $days_to_keep days archived to: $archive_name"


## Scheduling Tasks with Cron:
### This creates a cron job to run a script every hour.

        # Edit crontab (use 'crontab -e')
        # Add this line:
        0 * * * * /path/to/your_script.sh

