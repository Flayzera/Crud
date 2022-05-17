import http from "../http-common";
class TaskDataService {
  getAll(filters=null) {
    if(!filters)
      return http.get("/tasks/list/");
    else
      return http.get(`/tasks/list/${filters}`);
  }
  create(data) {
    return http.post("/tasks/create/", data);
  }
  update(id, data) {
    return http.patch(`/tasks/update/${id}/`, data);
  }
  delete(id) {
    return http.delete(`/tasks/update/${id}/`);
  }
}
export default new TaskDataService();