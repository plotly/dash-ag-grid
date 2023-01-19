import React from 'react';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm'

import ReactMarkdown from 'react-markdown';

export default function MarkdownRenderer(props) {
    // Markdown renderer with HTML rendering enabled.
    // rehypeRaw allows HTML rendering.
    // Convert <p> tags to simple <divs> using the components prop.
    const rehypePlugins = props.colDef.dangerously_allow_html ? [rehypeRaw] : []

    return (
        <ReactMarkdown
        linkTarget={props.colDef.linkTarget || '_self'}
        remarkPlugins={[[remarkGfm, {singleTilde: false}]]}
        components={{p: 'div',
            a: ({ node, children, ...props}) => {
                const linkProps = props;
                if (props.target === '_blank') {
                    linkProps['rel'] = 'noopener noreferrer';
                }
                return <a {...linkProps}>{children}</a>
            }
        }}
        className={'agGrid-Markdown'}
        rehypePlugins={rehypePlugins}
        children={String(props.value)}
        />
    );
}
