# Netbox Nbservice
[Netbox](https://github.com/netbox-community/netbox) Plugin for ITSM service mapping.

## Compatibility


| Plugin Version | NetBox Version | Tested on                      |
| ------------- |:-------------| :-----:|
| 1.0.7          | < 3.2.1                | 2.10.6; 2.11.12; 3.1.11; 3.2.1 |
| 2.0.0          | > 3.7.0, < 3.7.8       | 3.7.0, 3.7.4                   |
| 3.0.0          | > 4.0.0                | 4.0.7                          |
| 4.0.0          | > 4.1.0                | 4.1.0, 4.1.4                   |
| 4.2.0          | > 4.2.0                | 4.2.0                          |

## Installation

Add the following line to /opt/netbox/local_requirements.txt with
```
nb-service
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['nb_service']
```

Runs /opt/netbox/upgrade.sh

```
sudo /opt/netbox/upgrade.sh
```

## Features

### Service Management
- **Status Tracking**: Track service operational status (Active, Inactive, Deprecated, Planned) with color-coded badges
- **Criticality Levels**: Assign business criticality (Critical, High, Medium, Low) with visual indicators
- **Dependency Mapping**: Visualize upstream dependencies and downstream dependents
- **Auto-IC Creation**: Infrastructure Components are automatically created when new services are added
- **Quick Actions**: Fast access to create relations and add components via convenient UI buttons

### Global Service Diagram
Access a centralized view of all service relationships at `/plugins/nb_service/diagram/`
- Interactive Mermaid.js-powered topology diagram
- Shows all service dependencies across your infrastructure
- Clickable nodes to navigate to service details

### Cross-Service Relations
Create relationships between Infrastructure Components across different services for complete dependency mapping.

### Grafana Integration
Expose service relationships via REST API for monitoring dashboards:
- **Endpoint**: `/api/plugins/nb_service/graph/`
- **Format**: Grafana Node Graph compatible JSON (nodes + edges)
- Use with Prometheus/cAdvisor metrics for real-time service health visualization

### API Support
Full REST API access for all plugin features:
- Services: `/api/plugins/nb_service/services/`
- Applications: `/api/plugins/nb_service/applications/`
- Relations: `/api/plugins/nb_service/relations/`
- Infrastructure Components: `/api/plugins/nb_service/ics/`

## Configuration

```python
PLUGINS_CONFIG = {
    "nb_service": {
        "top_level_menu": True # If set to True the plugin will add a top level menu item for the plugin. If set to False the plugin will add a menu item under the Plugins menu item.  Default is set to True.
    },
}
```

# Screenshots

## Versions 2.X

### Service List

![](docs/2_x_SvList.png)

### Service View

![](docs/2_x_SvView.png)

### Service Relations

![](docs/2_x_SvRelation.png)

### Service Diagram

![](docs/2_x_SvDiagram.png)

### Application List

![](docs/2_x_AppList.png)

### Application View

![](docs/2_x_AppView.png)

### Application Devices

![](docs/2_x_AppDevices.png)

## Versions 3.X

### Service List

![](docs/3_x_SvList.png)

### Service View

![](docs/3_x_SvView.png)

### Service Relations

![](docs/3_x_SvRelation.png)

### Service Diagram

![](docs/3_x_SvDiagram.png)

### Application List

![](docs/3_x_AppList.png)

### Application View

![](docs/3_x_AppView.png)

### Application Devices

![](docs/3_x_AppDevices.png)
