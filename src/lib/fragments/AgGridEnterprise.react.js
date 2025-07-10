import React from 'react';
import {LicenseManager} from 'ag-grid-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

export default function DashAgGridEnterprise(props) {
    const {licenseKey} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    return <MemoizedAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
