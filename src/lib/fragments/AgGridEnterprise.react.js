import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {
    AllEnterpriseModule,
    IntegratedChartsModule,
    LicenseManager,
    SparklinesModule,
} from 'ag-grid-enterprise';
import {AgChartsCommunityModule} from 'ag-charts-community';
import {AgChartsEnterpriseModule} from 'ag-charts-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

// Register all enterprise features
ModuleRegistry.registerModules([
    AllEnterpriseModule,
    SparklinesModule.with(AgChartsEnterpriseModule),
]);

export default function DashAgGridEnterprise(props) {
    const {licenseKey, dashEnableCharts} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    if (dashEnableCharts) {
        if (dashEnableCharts === 'enterprise') {
            ModuleRegistry.registerModules([
                IntegratedChartsModule.with(AgChartsEnterpriseModule),
            ]);
        } else {
            ModuleRegistry.registerModules([
                IntegratedChartsModule.with(AgChartsCommunityModule),
            ]);
        }
    }
    return <MemoizedAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
