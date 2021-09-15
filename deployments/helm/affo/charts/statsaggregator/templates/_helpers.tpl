{{/*
Expand the name of the chart.
*/}}
{{- define "statsaggregator.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "statsaggregator.appVersion" -}}
{{- default .Chart.AppVersion .Values.appVersionOverride | quote }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "statsaggregator.fullname" -}}
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
{{- define "statsaggregator.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "statsaggregator.labels" -}}
helm.sh/chart: {{ include "statsaggregator.chart" . }}
{{ include "statsaggregator.selectorLabels" . }}
app.kubernetes.io/version: {{ include "statsaggregator.appVersion" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "statsaggregator.selectorLabels" -}}
app.kubernetes.io/name: {{ include "statsaggregator.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
auth: bearer
{{- end }}
