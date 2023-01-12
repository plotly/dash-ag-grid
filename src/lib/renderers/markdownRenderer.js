import React from 'react';
import rehypeRaw from 'rehype-raw';

import ReactMarkdown from 'react-markdown';

export default function MarkdownRenderer(props) {
    // Markdown renderer with HTML rendering enabled.
    // rehypeRaw allows HTML rendering.
    // Convert <p> tags to simple <divs> using the components prop.

    return (
        <ReactMarkdown components={{p: 'div'}} rehypePlugins={[rehypeRaw]}>
            {props.value}
        </ReactMarkdown>
    );
}
