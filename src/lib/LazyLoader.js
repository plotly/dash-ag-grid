export default {
    agGrid: () =>
        import(/* webpackChunkName: "community" */ './fragments/AgGrid.react'),
    agGridCharts: () =>
        import(
            /* webpackChunkName: "community-charts" */ './fragments/AgGridCharts.react'
        ),
    agGridEnterprise: () =>
        import(
            /* webpackChunkName: "enterprise" */ './fragments/AgGridEnterprise.react'
        ),
};
