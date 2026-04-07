import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {
    AllEnterpriseModule,
    IntegratedChartsModule,
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

let chartsModuleRegistered = false;

export default function DashAgGridEnterprise(props) {
    const {licenseKey, dashEnableCharts} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    if (dashEnableCharts && !chartsModuleRegistered) {
        ModuleRegistry.registerModules([
            IntegratedChartsModule.with(AgChartsEnterpriseModule),
        ]);
        chartsModuleRegistered = true;
    }
    return <MemoizedAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
