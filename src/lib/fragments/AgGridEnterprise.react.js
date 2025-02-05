import React, {Component} from 'react';
import {
    LicenseManager,
    AllEnterpriseModule,
    ModuleRegistry,
} from 'ag-grid-enterprise';
import DashAgGrid, {propTypes} from './AgGrid.react';

ModuleRegistry.registerModules([AllEnterpriseModule]);

export default class DashAgGridEnterprise extends Component {
    render() {
        const {licenseKey} = this.props;
        if (licenseKey) {
            LicenseManager.setLicenseKey(licenseKey);
        }
        return <DashAgGrid {...this.props} />;
    }
}

DashAgGridEnterprise.propTypes = propTypes;
