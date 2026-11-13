"""Render structured exam answers with shared study UI classes."""
from html import escape


def render_blocks(blocks, render_figure):
    result = []
    for block in blocks:
        kind = block['type']
        if kind == 'paragraph':
            result.append('<p>' + escape(block['text']) + '</p>')
        elif kind == 'list':
            result.append('<p><strong>' + escape(block['title']) + '</strong></p><ul>'
                          + ''.join('<li>' + escape(x) + '</li>' for x in block['items']) + '</ul>')
        elif kind == 'equation':
            result.append('<p><strong>' + escape(block['title']) + '</strong></p>'
                          + '<div class="source-equation">\\[' + escape(block['latex']) + '\\]</div>')
        elif kind == 'table':
            result.append('<div class="source-table-scroll" role="region" aria-label="Answer comparison" tabindex="0"><table><thead><tr>'
                          + ''.join('<th scope="col">' + escape(x) + '</th>' for x in block['headers'])
                          + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + escape(x) + '</td>' for x in row)
                          + '</tr>' for row in block['rows']) + '</tbody></table></div>')
        elif kind == 'figure':
            result.append(render_figure(block['id']))
        else:
            raise ValueError('Unknown study block: ' + kind)
    return ''.join(result)
