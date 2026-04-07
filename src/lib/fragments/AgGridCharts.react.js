import React from 'react';
import {ModuleRegistry} from 'ag-grid-community';
import {IntegratedChartsModule} from 'ag-grid-enterprise';
import {AgChartsCommunityModule} from 'ag-charts-community';
import {AgChartsEnterpriseModule} from 'ag-charts-enterprise';
import MemoizedAgGrid, {propTypes} from './AgGrid.react';

const chartsModules = {
    community: AgChartsCommunityModule,
    enterprise: AgChartsEnterpriseModule,
};

function getRegisteredChartModules() {
    if (typeof window === 'undefined') {
        return new Set();
    }
    if (!window.dashAgGridRegisteredChartModules) {
        window.dashAgGridRegisteredChartModules = new Set();
    }
    return window.dashAgGridRegisteredChartModules;
}

function registerChartsModule(mode) {
    const registeredChartModules = getRegisteredChartModules();
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
