# Famicom Disk System Header Remover

This script automates the removal of Famicom Disk System headers. Some ROMs contain headers that can trip up applications or hardware that expect headerless ROM files (like the Analogue NT Mini Noir). To be more specific, if the script detects a header starting with the text `FDS`, it will strip off the first 16 bytes of the file.

## Prerequisites

This script uses Python so you must have it installed.

## Usage

Place some number of Famicom Disc System ROM files in the `fds_roms` folder. It's ok to place the files in nested folders as the script will process files, recursively, within folders as well.

Example:

```code
fds_roms/
└──3 Famicom Disk System/
   ├──Japan/
   │  ├──Rom1.fds
   │  └──Rom2.fds
   ├──4 FDS Homebrew/
   │  ├──Rom1.fds
   │  └──Rom2.fds
   └──4 FDS Translations/
      ├──Rom1.fds
      └──Rom2.fds
```

Run the script:

`python fds_header_cleaner.py`

Any ROMs with headers will have the headers removed and placed in the `headerless_roms` folder. And ROMs without headers will just be copied to the `headerless_roms` folder. So, once this script finishes, the `headerless_roms` folder will contain all of the ROMs from the `fds_roms` folder without headers.
