# Use ansible to send configuration backup to gitlab

# Reference: https://github.com/Onemind-Services-LLC/EventDrivenAutomation-POC/blob/main/11_config_backup_gitlab.yml

```yaml
---
- name: Backup configuration of devices in dc_group
  hosts:  vyos1-site2,vyos2-site2
  gather_facts: no
  tasks:
    - name: configurable backup path
      vyos.vyos.vyos_config:
        backup: yes
        backup_options:
          filename: {{ inventory_hostname }}.cfg
          dir_path: ./vyos_backups

    - name: Commit to GitLab
      delegate_to: localhost
      uri:
        url: https://gitlab.com/api/v4/projects/{{gitlab_id}}/repository/commits
        headers:
          Private-Token: "{{ gitlab_token }}"
        method: POST
        validate_certs: false
        body: 
          branch: main
          commit_message: cisco config
          actions:
            - action: create
              file_path: "{{ inventory_hostname }}_backup.txt"
              content: "{{ file_content }}"
            # - action: create
            #   file_path: "R1_backup.txt"
            #   content: "{{ file_content }}"
            # - action: create
            #   file_path: "R2_backup.txt"
            #   content: "{{ file_content }}"            
        status_code: 201
        body_format: json
```

### Execute the above playbook

```
ansible-playbook -i inventory.ini your_playbook.yml
```
