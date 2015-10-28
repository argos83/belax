package config;

public class RedmineConfig extends BaseConfig {

    public static RedmineConfig config = new RedmineConfig();

    private RedmineConfig(){
        super("redmine");
    }

    public String getBaseURL(){
        return (String) settings.get("baseUrl");
    }
}
