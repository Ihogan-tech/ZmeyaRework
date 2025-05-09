# ZmeyaRework
Rework of Zmeya anti-virus engine with personal edits and various quality of life improvements.

Zmeya utilizes the ClamAV API to scan all files within a selected folder (or an entire machine with the full scan feature); using a custom hash and key algorithm, Zmeya locks up and quarantines dangerous files that can be reclaimed at the user's convenience with the unlock feature.

To run the program, download all files and run main.py in the UI folder.

On initial launch, navigate to settings and select 'Update Signatures' in order to create and/or update the database folder within the ClamAV folder.
