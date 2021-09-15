import * as React from "react";
import LinkIcon from '@material-ui/icons/Link';
import EqualizerIcon from '@material-ui/icons/Equalizer';
import { Admin, Resource } from 'react-admin';

import dataProvider from "./dataProvider";
import authProvider from './authProvider';

import { DeeplinkList, DeeplinkCreate } from './deeplinks';
import { StatsList } from './stats';

const App = () => (
  <Admin dataProvider={dataProvider} authProvider={authProvider} >
    <Resource name="deeplinks" list={DeeplinkList} create={DeeplinkCreate} icon={LinkIcon} />
    <Resource name="funnel/daily"  options={{ label: "Statistics" }} list={StatsList} icon={EqualizerIcon} />
  </Admin>
);

export default App;
