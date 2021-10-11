## Docker mühitində Linux quraşdırılması

1. Docker mühitini quraşdırın
1. Terminalda docker qovluğuna keçid alın
1. `docker-compose up --build -d` əmrini icra edin, bu zaman 2 ədəd CentOS və 1 ədəd Ubuntu container qalxmış olacaq
1. `docker ps -a` ilə container-lərin siyahısına baxın və container-ə daxil olmaq üçün, `docker exec -it naa1 bash` icra edin.
1. Container-ləri silmək üçün `docker-compose down --rmi all` əmrini icra edin

---

[Docker əmrlərinin qısa siyahısı](https://gist.github.com/mamedshahmaliyev/00abcd4c61fa3b9b226c5f8bd3ff2d26#file-docker_usefull_commands-sh) ilə tanış olun