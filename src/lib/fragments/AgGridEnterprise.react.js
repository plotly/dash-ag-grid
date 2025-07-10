import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {
    AllEnterpriseModule,
    LicenseManager,
    SparklinesModule,
} from 'ag-grid-enterprise';
import {AgChartsEnterpriseModule} from 'ag-charts-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

// Register all enterprise features
ModuleRegistry.registerModules([
    AllEnterpriseModule,
    SparklinesModule.with(AgChartsEnterpriseModule),
]);

export default function DashAgGridEnterprise(props) {
    const {licenseKey} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    return <MemoizedAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
