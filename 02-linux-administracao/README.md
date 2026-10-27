# 02-linux-administracao

Área de estudo de Python aplicada a Linux, engenharia e infraestrutura.

## Subáreas
- `gerenciamento-de-sistema/` — psutil, distro — métricas do sistema e identificação da distribuição.
- `systemd-e-servicos/` — subprocess, dbus-next — interação com systemd via comandos ou D-Bus.
- `pacotes-e-repositorios/` — subprocess — automação de apt/dnf; use os gerenciadores nativos do sistema.
- `discos-e-filesystems/` — psutil, pyudev — uso de discos e eventos de dispositivos.
- `usuarios-e-grupos/` — pwd, grp, subprocess — consulta de usuários/grupos e integração com ferramentas Linux.
- `logs-e-journald/` — subprocess, systemd-python (quando disponível) — consulta de logs e journald.

Instale dependências em um ambiente virtual por projeto; não instale tudo globalmente.
