# Specify parent image. Please select a fixed tag here.
ARG BASE_IMAGE=registry.git.
FROM ${BASE_IMAGE}

# Install packages via requirements.txt
ADD requirements.txt .
RUN pip install -r requirements.txt

# .. Or update conda base environment to match specifications in environment.yml
ADD environment.yml /tmp/environment.yml

# All packages specified in environment.yml are installed in the base environment
RUN conda env update -f /tmp/environment.yml && \
    conda clean -a -f -y
