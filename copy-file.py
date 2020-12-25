#!/Users/robertpoenaru/.pyenv/shims/python
import os
import subprocess
import glob

# create a copy of the file

# file_name = subprocess.run(
#     ['cp', './latex-content/my_prc.tex', './latex-content/my_prc_preprint.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


with open('my_prc.tex', 'rt') as draft:
    preprint = open('my_prc_preprint.tex', 'wt')
    lines = draft.readlines()
    count = 1
    for line in lines:
        if(count == 2):
            newline = 'preprint,\n'
            preprint.write(newline)
        else:
            preprint.write(line)
        count = count+1
    preprint.close()

paper_draft_mode = True
# draft mode
if(paper_draft_mode):
    try:
        # f=open("out.dat","w+")
        # subprocess.check_output(
        #     ['rm', '*.pdf'], stderr=subprocess.PIPE)
        proc = subprocess.Popen(
            ['pdflatex', 'my_prc.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
    # ['ls', './dir'], capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError:
        print(err.decode())
        # print(e.stderr.decode())
    else:
        print(out.decode())


paper_preprint_mode = True
# preprint mode
if(paper_preprint_mode):
    try:
        # f=open("out.dat","w+")
        # subprocess.check_output(
        #     ['rm', '*.pdf'], stderr=subprocess.PIPE)
        proc = subprocess.Popen(
            ['pdflatex', 'my_prc_preprint.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
    # ['ls', './dir'], capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError:
        print(err.decode())
        # print(e.stderr.decode())
    else:
        print(out.decode())


log_files = glob.glob('*.log', recursive=True)
aux_files = glob.glob('*.aux', recursive=True)
bib_files = glob.glob('*.bib', recursive=True)
pdf_files = glob.glob('*.pdf', recursive=True)

for f in log_files:
    try:
        os.unlink(f)
    except OSError as e:
        print(f'Cannot delete file: {e.strerror}')
    finally:
        print('Finished cleaning logs')

for f in bib_files:
    try:
        os.unlink(f)
    except OSError as e:
        print(f'Cannot delete file: {e.strerror}')
    finally:
        print('Finished cleaning bibs')

for f in aux_files:
    try:
        os.unlink(f)
    except OSError as e:
        print(f'Cannot delete file: {e.strerror}')
    finally:
        print('Finished cleaning aux')

abs_clean = False

if (abs_clean == True):
    print('Doing hard clean...')
    for f in pdf_files:
        try:
            os.unlink(f)
        except OSError as e:
            print(f'Cannot delete file: {e.strerror}')
        finally:
            print('Finished cleaning pdf')
