# Youtube Watch History Parser

## Instructions for acquiring YT watched data
- Go to the following site: https://takeout.google.com/settings/takeout
- Click on "Deselect all"
- Scroll down to Youtube and Youtube Music, click on the "All Youtube Data Included"
- Deselect all again, and only select "history"
- Continue and receive the export in whatever manner is best, download zip file
- ZIP file contains both search and watch history, extract watch history

## Executing this code
- Requires python3, beautifulsoup4
- If you need beautifulsoup4, pip3 install bs4
- replace list of files in filelist with whatever files you are running through the parser
- Program currently returns top 100 watched videos in the files - this can be adjusted via the array index slice in line 16
