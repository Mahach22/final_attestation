**Данный проект создан в рамках выполнения итогового задания № 10**
---

**Задание 10. Развертывание MySQL с использованием Kubernetes Operator в Minikube** <br>

Цель: Научиться разворачивать и управлять базой данных MySQL с использованием Kubernetes Operator в Minikube. В этом задании Вы развернете MySQL Operator и создадите MySQL-кластер.

**Описание задания:** <br>
* Запустите Minikube с достаточными ресурсами.
* Установите Helm, если он еще не установлен, и добавьте репозиторий для MySQL Operator.
* Установите MySQL Operator с использованием Helm.
* Создайте файл mysql-cluster.yaml для развертывания MySQL-кластера.
* Используйте следующие настройки: <br>

replicas: 3 — создает кластер с тремя репликами MySQL. <br>
mysqlVersion: "8.0" — устанавливает версию MySQL. <br>
backupSchedule: "*/5 * * * *" — планирует автоматическое резервное копирование каждые 5 минут. <br>

А вот куда их необходимо вставить, Вам необходимо разобраться.

* MySQL Operator требует наличие секрета, содержащего учетные данные для MySQL, создайте его.
* Зайдите в MySQL, проведите там некоторое время, а потом откатите БД к прошлому состоянию бекапа.
* MySQL Operator автоматически создает резервные копии согласно расписанию, заданному в backupSchedule.

В качестве решения Вам необходимо предоставить mysql_cluster.yaml, а также предоставить 2 команды — список резервных копий и восстановление из резервной копии. <br>

Результат задания — после выполнения задания у Вас будет развернут и настроен MySQL-кластер с использованием MySQL Operator в Minikube. Вы научитесь управлять кластером, выполнять резервное копирование и восстановление базы данных.

---

**Решение согласно условию задания:** <br>

[mysql-cluster.yaml](https://github.com/Mahach22/final_attestation/blob/main/10/mysql-cluster.yaml)

Выполнение команды для просмотра списка резервных копий



Выполнение команды для восстановления из резервной копии

Проверьте список резервных копий:
```
kubectl get mysqlbackups
```
Выберите нужную резервную копию и выполните восстановление:
```
kubectl apply -f - <<EOF
apiVersion: mysql.oracle.com/v2
kind: MySQLRestore
metadata:
  name: restore-backup
  namespace: default
spec:
  clusterRef:
    name: mysql-cluster
  backupRef:
    name: <имя_резервной_копии>
EOF
```
Подождите завершения процесса восстановления:
```
kubectl get mysqlrestore restore-backup
```




---

**Подробное выполнение задания:** <br>

Minikube у нас запущен, Helm установлен.

Добавляем репозиторий для MySQL Operator:
```
helm repo add mysql-operator https://mysql.github.io/mysql-operator/
helm repo update
```
Устанавливаем MySQL Operator с использованием Helm:
```
helm install mysql-operator mysql-operator/mysql-operator --namespace mysql-operator --create-namespace
```



Создаем секрет в соответствии с официальной документацией для нашего MySQL 
```
kubectl create secret generic mysql-secret \
        --from-literal=rootUser=root \
        --from-literal=rootHost=% \
        --from-literal=rootPassword="sakila"
```

Создаем конфигурацию для MySQL кластера [mysql-cluster.yaml](https://github.com/Mahach22/final_attestation/blob/main/10/mysql-cluster.yaml).
Применяем манифест:
```
kubectl apply -f mysql-cluster.yaml
```
Проверяем статус
```
kubectl get innodbclusters -n default 
```


Вход в MySQL и работа с базой данных
Чтобы зайти в MySQL, используйте pod, созданный MySQL Operator. Сначала найдите pod:
```
kubectl get pods -l app=mysql
```
Затем выполните подключение:
```
kubectl exec -it <pod-name> -- mysql -u root -p
```
Работайте с базой данных: создавайте таблицы, добавляйте данные, выполняйте запросы.


**Откат БД к предыдущему состоянию** <br>
MySQL Operator создаст автоматические резервные копии. Для отката:
Проверьте список резервных копий:
```
kubectl get mysqlbackups
```
Выберите нужную резервную копию и выполните восстановление:
```
kubectl apply -f - <<EOF
apiVersion: mysql.oracle.com/v2
kind: MySQLRestore
metadata:
  name: restore-backup
  namespace: default
spec:
  clusterRef:
    name: mysql-cluster
  backupRef:
    name: <имя_резервной_копии>
EOF
```
Подождите завершения процесса восстановления:
```
kubectl get mysqlrestore restore-backup
```

