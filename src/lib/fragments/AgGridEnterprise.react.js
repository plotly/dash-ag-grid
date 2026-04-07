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

function shouldRegisterChartsModule() {
    if (typeof window === 'undefined') {
        return true;
    }
    if (window.dashAgGridEnterpriseChartsRegistered) {
        return false;
    }
    window.dashAgGridEnterpriseChartsRegistered = true;
    return true;
}

export default function DashAgGridEnterprise(props) {
    const {licenseKey, dashEnableCharts} = props;
    if (licenseKey) {
        LicenseManager.setLicenseKey(licenseKey);
    }
    if (dashEnableCharts && shouldRegisterChartsModule()) {
        ModuleRegistry.registerModules([
            IntegratedChartsModule.with(AgChartsEnterpriseModule),
        ]);
    }
    return <MemoizedAgGrid {...props} />;
}

DashAgGridEnterprise.propTypes = propTypes;
