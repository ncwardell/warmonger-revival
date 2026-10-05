# Wiki build

The wiki is the `docs/` folder: Markdown with Obsidian `[[wikilinks]]` and callouts. Open `docs/` as an Obsidian vault to edit it.

It is published to GitHub Pages with [Quartz](https://quartz.jzhao.xyz) by `.github/workflows/pages.yml`, which fetches Quartz at the pinned commit below, copies `docs/` into its `content/`, applies `quartz.config.yaml` from this folder, and builds.

Preview locally:

```bash
git clone https://github.com/jackyzha0/quartz.git /tmp/quartz && cd /tmp/quartz
git checkout 97a2d05 && npm ci
rm -rf content && cp -r <repo>/docs content && cp <repo>/wiki/quartz.config.yaml .
npx quartz plugin install && npx quartz build --serve
```
