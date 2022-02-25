# Password Manager 2.0

This is the entire new version of the [Password manager](https://github.com/anirudhp06/Password_Manager)

The entire working of manger is changed now.


## Change Logs
1. Added functionality to Store encrypted passwords to database and not a text file.
2. Slightly Tweaked the display options.
3. Removed dependancy on a text file to store passwords.
> Using text file had risk of accidentally deleting it, resulting in loss of stored passwords.

Everything works the same but the only thing that is changed is instead of password storing in text file known as `passwords.txt` it will now be stored in database securely.

# Requirements:
1. MySQL
    - If you are on latest version of Windows 10 u can use the command to download the installer,
     `winget install mysql` or you can also download the community verision from [here](https://dev.mysql.com/downloads/installer/)
    
2. Python(3.6+)
    - You can download python from [windows store](https://www.microsoft.com/en-in/p/python-39/9p7qfqmjrfp7) or from their [website](https://www.python.org/downloads/)


3. `mysql.connector` module
    - This module will be installed automatically during installation of MySQL community edition, if still the problem exists just use command `pip install mysql-connector-python`

4. `cryptography` module
    - This module will be installed once you run the program first time.

    

Will update the wiki once I finish writing it... Please keep an eye on it.
