# PyCon Workshop: Machine Learning Pipeline Deployment with Kubeflow

Welcome to our PyCon Workshop on deploying Machine Learning pipelines with Kubeflow. This workshop will guide you through the process of preparing, compiling, deploying, and running a Machine Learning pipeline, utilizing a specific problem statement and dataset.

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.x
- `pip` for Python3


Please refer to the [Additional Resources](#additional-resources) section for detailed installation guides.

## Problem Statement & Dataset Information

### Overview

This workshop centers around a dataset featuring around 10 years of daily weather observations from several Australian weather stations. The challenge? To predict whether it will rain the following day.

### Objective

Your task is to predict the binary outcome `RainTomorrow`—`Yes` for rain, `No` for no rain—using the weather observations provided in the dataset.

### Dataset Description
- **Dataset URL:** http://rattle.togaware.com/weatherAUS.csv


The dataset comprises various weather measurements across multiple columns:

- **Date:** Observation date
- **Location:** Weather station location
- **MinTemp to MaxTemp:** Temperature metrics
- **Rainfall:** Daily rainfall
- **Evaporation:** Evaporation rate
- **Sunshine:** Sunshine hours
- **WindGustDir to WindGustSpeed:** Wind gust metrics
- **WindDir9am to WindDir3pm:** Wind direction at 9am and 3pm
- **WindSpeed9am to WindSpeed3pm:** Wind speed at 9am and 3pm
- **Humidity9am to Humidity3pm:** Humidity percentages
- **Pressure9am to Pressure3pm:** Atmospheric pressure
- **Cloud9am to Cloud3pm:** Cloud coverage
- **Temp9am to Temp3pm:** Temperatures at 9am and 3pm
- **RainToday:** Indicates if it rained today
- **RISK_MM:** Amount of rain that did not evaporate
- **RainTomorrow:** Target variable indicating if it will rain the next day

Using Linear Regression with `scikit-learn` (version `1.0.1`), you will predict `RainTomorrow` based on these features.

## Workshop Instructions

### Setting Up

Ensure you have `kfp` version `2.7.0` installed for compiling and deploying your machine learning pipelines:

```bash
pip install kfp==2.7.0
```


## Compiling the Pipeline

Once your code is ready, you'll need to compile it into a pipeline `.yaml` file using the Kubeflow Pipelines SDK. Here's how you can do it:

```bash
kfp dsl compile --py <input_python_file> --output <output_yaml_file>
```

Replace <input_python_file> with the name of your Python file containing the pipeline definition, and <output_yaml_file> with the desired output filename for the YAML file.

## Deploying the Pipeline

### Accessing the Kubeflow Dashboard

To deploy your compiled pipeline, navigate to the Kubeflow dashboard using the following link:

***http://52.57.146.252:8080/***

Use the following credentials to log in:

- **Username:** user@example.com
- **Password:** 12341234

### Uploading and Deploying Your Pipeline

Once logged in, follow these steps to upload and deploy your pipeline:

1. Navigate to the **Pipelines** tab in the navigation bar.
2. Click on **Upload pipeline** and select your compiled `.yaml` file.
3. Enter a name for your pipeline in the **Pipeline name** field.
4. Click **Create** to upload your pipeline.


## Creating a Run

To execute your pipeline:

1. From the dashboard, click on the **Create run** button.
2. Select "pycon-workshop-exp" as the experiment.
3. Set the required parameters for your pipeline run.
4. Click **Start** to initiate the run.


## Additional Resources

For those unfamiliar with some of the technologies used in this workshop, here are some resources to get you started:

- [Lightweight Python Components Documentation](https://www.kubeflow.org/docs/components/pipelines/v2/components/lightweight-python-components/)
- [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/)
- [Kubeflow Installation Guide](https://github.com/kubeflow/manifests)
- [Running the Kubeflow Dashboard](https://www.kubeflow.org/docs/components/central-dash/overview/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)

## Support

Should you encounter any issues or have questions during the workshop, please don't hesitate to reach out to the workshop organizers or raise an issue on this GitHub repository.
