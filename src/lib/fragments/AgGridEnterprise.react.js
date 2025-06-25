import React from 'react';
import {LicenseManager} from 'ag-grid-enterprise';
import DashAgGrid, {propTypes} from './AgGrid.react';

export default function DashAgGridEnterprise(props) {
    const {licenseKey} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    return <DashAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
