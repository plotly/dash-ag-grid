import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {AllEnterpriseModule, LicenseManager} from 'ag-grid-enterprise';
import DashAgGrid, {propTypes} from './AgGrid.react';

// Register all enterprise features
ModuleRegistry.registerModules([AllEnterpriseModule]);

export default function DashAgGridEnterprise(props) {
    const {licenseKey} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    return <DashAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
