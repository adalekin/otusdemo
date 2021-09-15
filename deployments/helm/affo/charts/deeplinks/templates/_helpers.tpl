{{/*
Expand the name of the chart.
*/}}
{{- define "deeplinks.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "deeplinks.appVersion" -}}
{{- default .Chart.AppVersion .Values.appVersionOverride | quote }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "deeplinks.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "deeplinks.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "deeplinks.labels" -}}
helm.sh/chart: {{ include "deeplinks.chart" . }}
{{ include "deeplinks.selectorLabels" . }}
app.kubernetes.io/version: {{ include "deeplinks.appVersion" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "deeplinks.selectorLabels" -}}
app.kubernetes.io/name: {{ include "deeplinks.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
auth: bearer
{{- end }}
