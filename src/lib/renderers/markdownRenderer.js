import React from 'react';
import PropTypes from 'prop-types';

import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';

import ReactMarkdown from 'react-markdown';

export default function MarkdownRenderer(props) {
    const {colDef, target, value, dangerously_allow_code} = props;
    // Markdown renderer with HTML rendering enabled.
    // rehypeRaw allows HTML rendering.
    // Convert <p> tags to simple <divs> using the components prop.
    const rehypePlugins = dangerously_allow_code ? [rehypeRaw] : [];

    let linkTarget;
    if (!dangerously_allow_code) {
        linkTarget = colDef.linkTarget || '_self';
    }

    return (
        <ReactMarkdown
            linkTarget={linkTarget}
            remarkPlugins={[[remarkGfm, {singleTilde: false}]]}
            components={{
                p: 'div',
                a: ({node: _, children, ...props}) => {
                    const linkProps = props;
                    if (target === '_blank') {
                        linkProps.rel = 'noopener noreferrer';
                    }
                    return <a {...linkProps}>{children}</a>;
                },
            }}
            className="agGrid-Markdown"
            rehypePlugins={rehypePlugins}
            children={value ? String(value) : null}
        />
    );
}

MarkdownRenderer.propTypes = {
    colDef: PropTypes.any,
    target: PropTypes.string,
    value: PropTypes.string,
    dangerously_allow_code: PropTypes.bool,
};
