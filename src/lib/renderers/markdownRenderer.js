import React from 'react';
import PropTypes from 'prop-types';

import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import rehypeExternalLinks from 'rehype-external-links';

import ReactMarkdown from 'react-markdown';

export default function MarkdownRenderer(props) {
    const {colDef, value, dangerously_allow_code} = props;
    // Markdown renderer with HTML rendering enabled.
    // rehypeRaw allows HTML rendering.
    // Convert <p> tags to simple <divs> using the components prop.
    const rehypePlugins = dangerously_allow_code ? [rehypeRaw] : [];

    let linkTarget;
    if (!dangerously_allow_code) {
        linkTarget = colDef.linkTarget || '_self';
    }

    rehypePlugins.push([
        rehypeExternalLinks,
        {target: linkTarget, rel: ['noopener', 'noreferrer', 'nofollow']},
    ]);

    return (
        <div className="agGrid-Markdown">
            <ReactMarkdown
                remarkPlugins={[[remarkGfm, {singleTilde: false}]]}
                components={{
                    p: 'div',
                    a({node: _, children, target, ...props}) {
                        const linkProps = props;
                        const subLinkTarget = linkTarget || target;
                        // Use the correct target for links
                        if (subLinkTarget === '_blank') {
                            linkProps.rel = 'noopener noreferrer nofollow';
                        }
                        return (
                            <a {...{target: subLinkTarget, ...linkProps}}>
                                {children}
                            </a>
                        );
                    },
                }}
                rehypePlugins={rehypePlugins}
                children={value ? String(value) : null}
            />
        </div>
    );
}

MarkdownRenderer.propTypes = {
    colDef: PropTypes.any,
    target: PropTypes.string,
    value: PropTypes.string,
    dangerously_allow_code: PropTypes.bool,
};
