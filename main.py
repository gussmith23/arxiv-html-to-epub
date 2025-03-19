import os
import subprocess
import tempfile


def main(url, filename):
    # Convert an Arxiv paper to an epub.
    # url: URL of the Arxiv paper.
    # filename: Filename to save the epub to.
    
    tmpdir = tempfile.mkdtemp()

    # Get the paper from the url using wget and --convert-links.
    previous_dir = os.getcwd()
    os.chdir(tmpdir)
    p = subprocess.run(["wget", "-E", "-H", "-k", "-K", "-p",  url])
    os.chdir(previous_dir)
    p.check_returncode()

    # Find the html file that was downloaded.
    html_files = [f for f in os.listdir(tmpdir + "/arxiv.org/html") if f.endswith(".html")]
    print(html_files)
    assert len(html_files) == 1
    html_file = tmpdir + "/arxiv.org/html/" + html_files[0]

    # Run pandoc to convert the html to epub.
    subprocess.run(["pandoc", "-o", filename, html_file], check=True)



if __name__ == "__main__":

    # Take two arguments: a url pointing to an html version of an Arxiv paper,
    # and a filename to save the resulting epub to.

    import argparse

    parser = argparse.ArgumentParser(description='Convert an Arxiv paper to an epub.')
    parser.add_argument('--url', type=str, help='URL of the Arxiv paper.')
    parser.add_argument('--filename', type=str, help='Filename to save the epub to.')
    args=parser.parse_args()

    main(args.url, args.filename)
