import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {
    AllEnterpriseModule,
    IntegratedChartsModule,
    LicenseManager,
    SparklinesModule,
} from 'ag-grid-enterprise';
import {AgChartsCommunityModule} from 'ag-charts-community';
import {
    AgChartsEnterpriseModule,
    LicenseManager as AgChartsLicenseManager,
} from 'ag-charts-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

// Register all enterprise features
ModuleRegistry.registerModules([
    AllEnterpriseModule,
    SparklinesModule.with(AgChartsEnterpriseModule),
]);

export default function DashAgGridEnterprise(props) {
    const {licenseKey, chartsLicenseKey, dashEnableCharts} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    if (dashEnableCharts) {
        if (dashEnableCharts === 'enterprise') {
            const effectiveChartsLicenseKey = chartsLicenseKey || licenseKey;
            if (effectiveChartsLicenseKey) {
                AgChartsLicenseManager.setLicenseKey(effectiveChartsLicenseKey);
            }
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
