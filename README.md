# OCR-Automater-GoogleDocumentCloud
Uploads files to Google Document Cloud for OCR-ifying, then spits them all out as one combined text document. For personal use. 

README

Running this will require some basic Python knowledge and some dependencies.

You'll need POPPLER and you'll need to be set up with Google Cloud Services. If anyone actually wants to know how to do that, make an issue and I'll see what I can do.

The TLDR for that: 
A. Create a Google Cloud Project.
B. Enable the Document AI API in Google Cloud Console.
C. Create a Document AI Processor (OCR). You should see it in the top menu.
D. Generate a Service Account Key . (Google it to find out how)
E. Go to IAM & Admin  -> Service Accounts.
D. Create a new JSON key and download it. (your-key.json).

As for Poppler and other dependencies you'll also want to install pdf2image and pillow and poppler-utils


There are a few fairly simple changes you'll need to make too, so open it up in your coding environment tool of choice. 

A. Replace Line 11's TKTKTKTK with your key location.
B. Change the project location (20)
C. cross your fingers 
D. change the output/input folder locations (that should be easy enough, lines 23/24)
E. good luck! when ready, run it by opening up cmd, going to the folder it's located in, and typing in the name. IE "py uploader-then-OCR-then-download-as-one-file.py" 
