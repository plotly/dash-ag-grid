import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {IntegratedChartsModule} from 'ag-grid-enterprise';
import {AgChartsCommunityModule} from 'ag-charts-community';
import {AgChartsEnterpriseModule} from 'ag-charts-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

const registeredChartModules = new Set();
const chartsModules = {
    community: AgChartsCommunityModule,
    enterprise: AgChartsEnterpriseModule,
};

function registerChartsModule(mode) {
    if (!registeredChartModules.has(mode)) {
        ModuleRegistry.registerModules([
            IntegratedChartsModule.with(chartsModules[mode]),
        ]);
        registeredChartModules.add(mode);
    }
}

export default function DashAgGridCharts(props) {
    const mode =
        props.dashEnableCharts === 'enterprise' ? 'enterprise' : 'community';
    registerChartsModule(mode);
    return <MemoizedAgGrid {...props} />;
}

DashAgGridCharts.propTypes = propTypes;
