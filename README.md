# project-files-formatter
# File Organizer Script  
###important note:
currently it only works in linux, and it moves every file. this will be changed in future updates
![File Organizer](https://via.placeholder.com/800x200.png?text=File+Organizer+Script)  

## Overview  

The **File Organizer Script** is a Python utility designed to help you automatically organize files in your directory based on their file types. Whether you're dealing with a cluttered downloads folder or managing project files, this script simplifies the process by sorting files into designated folders.  

### Features  

- **Cross-Platform Compatibility**: Works seamlessly on both Linux and Windows operating systems.  
- **Automatic Sorting**: Organizes files into predefined directories based on their extensions.  
- **Customizable**: Easily modify the file type mappings to suit your needs.  
- **Error Handling**: Robust error handling to ensure smooth execution.  

## How It Works  

The script scans the current directory and its subdirectories for files. It then categorizes each file based on its extension and moves it to the corresponding folder. The folder structure is predefined and can be customized in the script.  

### File Type Mapping  

The following file types are supported by default:  

- **Text Files**: `.txt` → `res/text/`  
- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg` → `res/image/`  
- **Documents**: `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx` → `res/word/`  
- **Archives**: `.zip`, `.tar`, `.gz`, `.rar` → `res/archives/`  
- **Audio/Video**: `.mp3`, `.mp4`, `.avi`, `.mkv` → `res/audio/`, `res/video/`  
- **Others**: Any unsupported file types will be moved to `res/others/`  

## Getting Started  

### Prerequisites  

- Python 3.x installed on your machine.  
- Basic knowledge of running Python scripts.  

### Installation  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/JavadiSM/project-files-formatter
   cd project-files-formatter