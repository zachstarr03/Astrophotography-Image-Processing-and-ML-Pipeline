# Astrophotography-Image-Processing-and-ML-Pipeline
An end-to-end Astrophotography Enhancement System. The tech stack for this project will consist of Python libraries for scientific computing, data science and exploration, computer vision, astronomy data processing, and software engineering. I am taking a modular architecture approach towards this project, and will be pushing new work onto this repo weekly.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Data Folder

The 'data/' folder contains four subfolders:
- 'bias/' -> Calibration bias frames (small FITS files, may be able to be tracked in Git if they're small enough)
- 'dark/' -> Dark frames (small FITS files, may be able to be tracked in Git if they're small enough)
- 'flat/' -> Flat frames (small FITS files, may be able to be tracked in Git if they're small enough)
- 'raw/' -> Raw FITS images (large FITS files, too large for Git)

### How to download raw FITS images

1.) I am using Hubble Legacy Archive to find raw FITS images. You can search for the object(s) you want, and download the raw FITS images of them.

2.) I am storing the raw FITS files I've downloaded from Hubble Legacy Archive on this Google Drive: https://drive.google.com/drive/folders/1der2ish36uNrb_wubRjaa48QEEYjBkHp?usp=drive_link

    - Place them in the 'data/raw/' folder
    - The directory structure should look like this:
      data/
        bias
        dark
        flat
        raw

### Also, make sure the filenames are preserved for the scripts and notebooks to work properly.
