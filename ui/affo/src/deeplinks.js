import * as React from "react";
import { List, Datagrid, TextField, UrlField, Create, SimpleForm, TextInput, required } from 'react-admin';

export const DeeplinkList = (props) => (
    <List pagination={false} {...props}>
        <Datagrid>
            <UrlField source="target_url" label="Target URL" />
            <UrlField source="url" label="URL" />
            <TextField source="cn" label="Campaign Name" />
            <TextField source="cs" label="Campaign Source" />
        </Datagrid>
    </List>
);

export const DeeplinkCreate = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="url" label="URL" validate={required()} />
            <TextInput source="cn" label="Campaign Name" />
            <TextInput source="cs" label="Campaign Source" />
        </SimpleForm>
    </Create>
);
