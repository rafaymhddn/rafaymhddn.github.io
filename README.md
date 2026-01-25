# Personal Website (Jekyll)

This is a Jekyll-powered personal website based on the Jekyll Now starter, with a layout inspired by Jon Barron's and Barry Clark site. You are welcome to use this template, but please do not reuse any personal content or media from this repository.

## Features
- Fast, static site hosted on GitHub Pages
- Simple page and post structure
- Easy theming with Sass in `_sass` and `style.scss`
- Custom pages under `_pages` and layouts in `_layouts`

## Quick start
1) Fork or clone this repository.
2) Install dependencies:
   ```bash
   bundle install
   ```
3) Run the site locally:
   ```bash
   bundle exec jekyll serve
   ```
4) Open `http://localhost:4000` in your browser.

## Customization
- Site settings: update `_config.yml` (title, description, base URL, social links).
- Content:
  - Posts live in `_posts` and follow the `YYYY-MM-DD-title.md` pattern.
  - Pages live in `_pages`.
- Assets:
  - Images in `images`
  - PDFs in `pdfs`
- Styling:
  - Sass partials in `_sass`
  - Main stylesheet in `style.scss`

## Deployment (GitHub Pages)
1) Push your changes to your GitHub repo.
2) In GitHub, go to Settings → Pages.
3) Select the branch you want to deploy (typically `main`) and the root folder.
4) GitHub Pages will build the site automatically.

## Content and attribution
- This repo is based on Jekyll Now: `https://github.com/barryclark/jekyll-now`
- Visual inspiration: `https://jonbarron.info/`
- Please remove or replace any personal content in `images`, `pdfs`, and `_posts`.
- If you reuse the template, a link back is appreciated.

## License
See `LICENSE`.
