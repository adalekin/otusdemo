import * as React from "react";
import LinkIcon from '@material-ui/icons/Link';
import EqualizerIcon from '@material-ui/icons/Equalizer';
import { fetchUtils, Admin, Resource, ListGuesser } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';

import authProvider from './authProvider';
import { StatisticsList } from './statistics';

const httpClient = (url, options = {}) => {
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }

  const accessToken = localStorage.getItem('access_token');
  options.headers.set('Authorization', `Bearer ${accessToken}`);
  return fetchUtils.fetchJson(url, options);
}

const dataProvider = jsonServerProvider('http://affo.arch.homework', httpClient);
const App = () => (
  <Admin dataProvider={dataProvider} authProvider={authProvider} >
    <Resource name="statistics" list={StatisticsList} icon={EqualizerIcon} />
    <Resource name="deeplinks" list={ListGuesser} icon={LinkIcon} />
  </Admin>
);

export default App;
