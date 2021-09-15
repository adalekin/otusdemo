import * as React from "react";
import { List, Datagrid, TextField, DateField } from 'react-admin';

export const StatsList = (props) => (
    <List {...props}>
        <Datagrid>
            <DateField source="date" />
            <TextField source="clicks" />
            <TextField source="registrations" />
            <TextField source="revenue" />
        </Datagrid>
    </List>
);