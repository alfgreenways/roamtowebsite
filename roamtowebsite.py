import json
import re
from slugify import slugify
import os


def find_index_page(all_pages):
    for page in all_pages:
        if page.get('title', '').lower() == 'index':
            return page


def render_page_content(page):
    content = ''
    for child in page.get('children', []):
        heading = page.get('heading', 0)
        string = child.get('string', '')

        # Parse links
        This is where I left off
        def replace(matchobj):
            import ipdb; ipdb.set_trace() 
            print(matchobj.group(0))
        string = re.sub(r'\[\[([^]]*)\]\]', replace, string)

        if heading > 0:
            content += f"\n<h{heading}>{string}</h{heading}>\n"
        else:
            content += f"\n<p>{string}</p>\n"
    return content



def page_to_html(page):
    title = page.get('title', '')
    slug = slugify(title).lower()
    content = render_page_content(page)
    return slug, (theme
        .replace('{{ page_title }}', title)
        .replace('{{ page_content }}', content)
    )


def roam_to_website(all_pages, theme):
    website_pages = {}
    for page in all_pages:
        slug, html = page_to_html(page)

        website_pages[slug] = html
    return website_pages


def clear_and_remake_public_folder():
    # safely delete and mkdir the /public folder
    pass


def write_public_file(slug, html):
    filename = f'./public/{slug}/index.html'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(html)
    if slug == 'index':
        with open(f'./public/index.html', 'w') as f:
            f.write(html)



if __name__ == '__main__':
    with open('alfgreenways.json', 'r') as f:
        all_pages = json.loads(f.read())
    with open('theme.html', 'r') as f:
        theme = f.read()
    website_pages = roam_to_website(all_pages, theme)

    index_page = website_pages['index']

    for slug, html in website_pages.items():
        print(f"Writing /{slug}/\n")
        write_public_file(slug, html)
    print("Done!")
