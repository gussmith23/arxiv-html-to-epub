# arxiv-html-to-epub

To use this repo, you should just be able to do the following:
1. Copy the repo, but in a way that allows you to open your own issues (e.g. don't just fork it). You may need to clone it locally, manually create a new repo on GitHub, and then push to that repo.
2. Open an issue on the repo and note its number. Set the environment variables in the workflow files (`.github/workflows/*.yml`) appropriately.
3. Submit papers via the workflow in the Actions tab. The papers should get posted as a comment on the issue.

My workflow using this repo is:
1. I have the link to the "submit paper" action bookmarked (for me, it's https://github.com/gussmith23/arxiv-html-to-epub/actions/workflows/run.yml). When I'm reading through lists of papers and see one I'm interested in, I find the Arxiv for it (hopefully it exists, usually it does), get the HTML link, and submit it to the workflow.
2. Later, when I have time to read, I pick a paper from the list and skim it.
3. When I'm done reading the paper, I react with a "+1" on the comment for the paper. Ideally, I also edit the comment with my own notes.
4. Sometime later, the pruning workflow runs (automatically or manually). All comments with a +1 from me get moved to the archived list of papers.
