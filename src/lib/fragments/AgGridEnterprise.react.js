import React, {Component} from 'react';
import {LicenseManager} from 'ag-grid-enterprise';
import DashAgGrid, {propTypes} from './AgGrid.react';

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
