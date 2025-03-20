# arxiv-html-to-epub

Converts papers on Arxiv to epubs for easy reading (+ maintains a reading list). Only uses GitHub Actions, no local code needed.

You should be able to quickly start using this repo for yourself.
To use this repo, you should just be able to do the following:
1. Copy the repo, but in a way that allows you to open your own issues (e.g. don't just fork it). You may need to clone it locally, manually create a new repo on GitHub, and then push to that repo.
2. Open two issues on the repo: one for your reading list, one for archived papers. Note the issue numbers.
3. Set the environment variables in the workflow files (`.github/workflows/*.yml`) appropriately (issue numbers, your username).
4. Submit papers via the workflow in the Actions tab. The papers should get posted as a comment on the issue.

This repo is another attempt at getting myself to read more papers.
For me, the main blocker in reading more papers is making it much faster and easier to start skimming a paper. It's something I'd like to be able to do when I have a few minutes, especially on my phone.
This approach hopefully solves that by converting interesting papers to epubs that can be easily read on my phone. It also makes it very easy to submit papers to my inbox when I find interesting papers.

My workflow using this repo is:
1. I have the link to the "submit paper" action bookmarked (for me, it's https://github.com/gussmith23/arxiv-html-to-epub/actions/workflows/run.yml). When I'm reading through lists of papers and see one I'm interested in, I find the Arxiv for it (hopefully it exists, usually it does), get the HTML link, and submit it to the workflow.
2. Later, when I have time to read, I pick a paper from the list and skim it.
3. When I'm done reading the paper, I react with a "+1" on the comment for the paper. Ideally, I also edit the comment with my own notes.
4. Sometime later, the pruning workflow runs (automatically or manually). All comments with a +1 from me get moved to the archived list of papers.
