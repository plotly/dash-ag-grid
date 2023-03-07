import React, {useCallback, useState} from 'react';
import PropTypes from 'prop-types';

import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Button from '@material-ui/core/Button';
import AddIcon from '@material-ui/icons/Add';

export default function RowMenuRenderer(props) {
    const [anchorEl, setAnchorEl] = useState(null);
    const {setData, data} = props;

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = useCallback(
        (e) => {
            const {
                target: {value},
            } = e;

            if (setData && value) {
                setData(value);
            }
            setAnchorEl(null);
        },
        [setData, data]
    );

    return (
        <div>
            <Button
                aria-controls="simple-menu"
                aria-haspopup="true"
                onClick={handleClick}
                variant="outlined"
            >
                <AddIcon />
            </Button>
            <Menu
                id="simple-menu"
                anchorEl={anchorEl}
                keepMounted
                open={Boolean(anchorEl)}
                onClose={handleClose}
            >
                {props.value.map((p) => (
                    <MenuItem onClick={handleClose} value={p.value}>
                        {p.label}
                    </MenuItem>
                ))}
            </Menu>
        </div>
    );
}

RowMenuRenderer.propTypes = {
    setProps: PropTypes.func,
    data: PropTypes.any,
    value: PropTypes.any
};
